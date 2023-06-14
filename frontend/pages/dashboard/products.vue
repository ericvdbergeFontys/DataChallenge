<template>
  <div>
    <h1>Products</h1>
    <br/>
    <n-grid class="grid" x-gap="30" :cols="12">
        <n-gi :span="2" class="container" v-for="product in products" :key="product">
          <Product :product="product" @click="changeModalState(product)"/>
        </n-gi>
    </n-grid>
    <AnalyticsModal v-if="showModal && selectedProduct != undefined" :showModal="showModal" :productName="selectedProduct"/>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'dashboard'
})

const products = await useProducts();
let showModal = ref(false)
let selectedProduct = ref()

const changeModalState = (product) => {
  showModal.value = true
  selectedProduct.value = product.label
}
</script>

<style scoped>
  .grid {
    column-gap: 30px !important;
    row-gap: 30px !important;
  }
</style>