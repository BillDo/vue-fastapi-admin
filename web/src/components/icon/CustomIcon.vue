<script setup>
/** Custom Icons */
const props = defineProps({
  /** Icon name (filename under assets/svg) */
  icon: {
    type: String,
    required: true,
  },
  size: {
    type: Number,
    default: 14,
  },
  color: {
    type: String,
    default: undefined,
  },
})
</script>

<template>
  <TheIcon type="custom" v-bind="props" />
</template>
