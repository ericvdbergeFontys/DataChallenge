<template>
    <n-modal v-model:show="props.showModal" preset="card" size="huge" :mask-closable="false" aria-modal="true">
      <template #header>
        <div style="margin-left: 10px">Review Analytics</div>
      </template>
      <template #header-extra>
        <button @click="() => props.showModal = false">close</button>
      </template>
      <div style="padding: 30px" id="analytics"></div>
    </n-modal>
  </template>
  
<script setup>
const analytics = useAnalytics();
onMounted(async () => {
  const Plotly = await import('plotly.js-basic-dist');
  if(props.productName != undefined) {
    
    const analyticsInfo = await analytics.getForProduct(props.productName)
    
    var data = [
      {
        x: Object.keys(analyticsInfo),
        y: Object.values(analyticsInfo),
        type: 'bar'
      }
    ];

    const layout = {
      width: 900,  // Specify the width of the plot in pixels
      height: 400  // Specify the height of the plot in pixels
    };

    Plotly.newPlot('analytics', data, layout);
  }
})

const props = defineProps({
  showModal: {
    Type: Boolean,
    default: false
  },
  productName: String
})

</script>

<style>
.n-modal {
  width: 50vw !important;
  height: 60vh !important;
}

#analytics, .plotly {
  width: calc(100% - 60px) !important;
  height: calc(300px - 60px)
}
</style>