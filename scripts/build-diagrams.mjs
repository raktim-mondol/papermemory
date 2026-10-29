#!/usr/bin/env node
/**
 * Render docs/diagrams/*.mmd to docs/assets/diagrams/*.svg with Pele (https://github.com/obsidianmd/pele),
 * a Mermaid renderer that needs no browser.
 *
 *   npm install --no-save pele      # once, anywhere on the module path
 *   node scripts/build-diagrams.mjs
 *
 * The SVGs are committed so the README renders on GitHub without a build step. Pele writes colours as CSS
 * variables; Inkscape, rsvg-convert, and CairoSVG do not resolve those and draw a blank image, so the
 * colours are flattened to literal values and a white background is added.
 */
import { mkdirSync, readdirSync, readFileSync, writeFileSync } from 'node:fs'
import { basename, extname, join } from 'node:path'
import { render } from 'pele'

const SOURCE_DIR = 'docs/diagrams'
const OUTPUT_DIR = 'docs/assets/diagrams'

function flattenColors(svg) {
  const props = new Map()
  for (const match of svg.matchAll(/(--[\w-]+)\s*:\s*([^;}"]+)/g)) {
    if (!props.has(match[1])) props.set(match[1], match[2].trim())
  }
  let out = svg
  for (let pass = 0; pass < 8 && out.includes('var('); pass += 1) {
    const next = out.replace(/var\(\s*(--[\w-]+)\s*(?:,\s*([^()]*))?\)/g, (_whole, name, fallback) => {
      const declared = props.get(name)
      if (declared != null && !declared.includes(name)) return declared
      return fallback != null ? fallback.trim() : ''
    })
    if (next === out) break
    out = next
  }
  return out
}

mkdirSync(OUTPUT_DIR, { recursive: true })
const sources = readdirSync(SOURCE_DIR).filter((name) => extname(name) === '.mmd').sort()
let failed = 0
for (const name of sources) {
  const target = join(OUTPUT_DIR, `${basename(name, '.mmd')}.svg`)
  try {
    const result = render(readFileSync(join(SOURCE_DIR, name), 'utf8'), { fontSize: 14, padding: 18, maxWidth: 1100 })
    const svg = flattenColors(result.svg).replace(/(<svg\b[^>]*>)/, '$1<rect width="100%" height="100%" fill="#ffffff"/>')
    writeFileSync(target, svg, 'utf8')
    console.log(`${name} -> ${target} (${result.width}x${result.height}, ${result.mermaidType})`)
  } catch (error) {
    failed += 1
    console.error(`${name}: ${error.message}${error.line ? ` (line ${error.line})` : ''}`)
  }
}
if (failed) process.exit(1)
