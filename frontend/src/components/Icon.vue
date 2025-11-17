<template>
  <component :is="iconComponent" />
</template>

<script setup>
import { computed, h } from 'vue'

const props = defineProps({
  name: {
    type: String,
    required: true,
  },
})

// For dynamic icons, we'll use a simple approach
// If icon name contains colon, try to parse it
const iconComponent = computed(() => {
  if (!props.name) return null
  
  // If it's a format like "material-symbols:category" or "mdi:package"
  // We'll render a placeholder or you can expand this to import icons dynamically
  // For now, return a simple SVG placeholder
  return () => h('svg', {
    viewBox: '0 0 24 24',
    fill: 'currentColor',
    width: '1em',
    height: '1em',
  }, [
    h('path', {
      d: 'M12 2L2 7L12 12L22 7L12 2Z',
    }),
  ])
})
</script>

