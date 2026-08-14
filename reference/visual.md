# The Visual Slop Reference

Visual slop is the design fingerprint of AI-generated products and sites. It is the reason experienced designers can spot a vibe-coded landing page in one glance. This reference catalogs the tells. For the curated ecosystem of visual-slop tools, see `ecosystem.md`.

## The seven tells

### 1. The purple-blue gradient

The single most identifiable visual tell. A purple-to-blue gradient (often on the hero background, CTA buttons, or both) is what LLMs default to for anything "modern." The signature: `#6366F1` to `#8B5CF6` to `#EC4899` ranges, usually blurred at 50% opacity.

Fix: Pick one brand color and use it flat. If you need depth, use it at different opacities.

### 2. The centered hero with generic headline

White background, centered column, 48px "Empower your workflow with AI-powered solutions" headline, subline, two buttons (one gradient, one outline), and a screenshot below. Every AI site ships this exact layout.

Fix: Left-align or asymmetric layouts. Lead with a specific claim. Show the product doing something real.

### 3. The blob / glassmorphism background

A blurred radial blob in the corner of the hero, or frosted-glass cards. Both are LLM visual defaults from image-model training data.

Fix: Use real photography, a product shot, or nothing. Glassmorphism reads as AI in 2026.

### 4. The generic 3-icon feature row

Three icons in circles (lucide defaults), three titles, three paragraphs. "Integrations", "Analytics", "Security" with the same three icons on every AI product site.

Fix: Show real features with real UI. Icons only where they communicate something.

### 5. The "trusted by" logo wall

A row of fake or generic logos in grayscale, usually from companies that never used the product. LLMs generate this section automatically.

Fix: Name real customers with permission, or drop the section.

### 6. The stock-photo testimonial

A headshot photo with a quote that reads like the person never said it. Usually paired with a 5-star rating row.

Fix: Use real testimonials with real names and roles, or write the quote in a voice that matches your actual customer.

### 7. The emoji-as-design-element

Emoji used as section icons, bullet markers, or decorative elements in UI. AI uses emoji as a cheap substitute for real iconography.

Fix: Use a real icon set (lucide, heroicons) or nothing.

## Typography tells

- **Inter or system font stack everywhere**: fine, but paired with default weights it reads template-y. Use a display font for headlines.
- **All-caps micro-labels**: "FEATURES", "ABOUT US" eyebrow labels above every section. AI's default way to add structure.
- **Overlapping gradient text**: `bg-clip-text` gradient headlines. Worn out.

## Layout tells

- **Symmetry everywhere**: every section centered, every card the same size, everything in perfect rows. Real products have organic asymmetry.
- **Card-everything**: every piece of content in a rounded-rectangle card with a border. AI cannot lay out content without a card.
- **Z-index soup**: overlapping elements with negative margins that accomplish nothing.

## The test

If you remove the gradient, the emoji, and the card borders and the design still communicates, it was never slop. If removing them leaves nothing, it was slop.
