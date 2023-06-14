<template>
    <n-card :title="product.label">
      <template #cover>
        <img src="/product-image.png">
      </template>
    </n-card>
</template>

<script setup>
const { product } = defineProps({
  product: {
    label: String
  }
})
</script>

<style lang="scss" scoped>
    .n-card {
        width: 100%;
        height: 100%;
        &:hover {
          box-shadow: 0px 3px 6px #ccc;
          cursor: poniter;
        }
    }
</style>