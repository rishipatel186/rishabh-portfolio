// One source of truth for the layout switch.
// At or below COMPACT_MAX the site uses the stacked layout with the photo hero
// (no 3D character, native scrolling). Above it, the full desktop experience.
// Keep this in sync with the `max-width: 1024px` queries in the CSS.
export const COMPACT_MAX = 1024;

export const isCompactViewport = (): boolean =>
  typeof window !== "undefined" && window.innerWidth <= COMPACT_MAX;
