<template>
  <div>
    <h1>Dashboard</h1>
    <br/>
    <n-grid class="grid" x-gap="30" :cols="12">
      <n-gi :span="5">
        <n-card title="TOP 5 WORST PRODUCTS">
          <n-data-table
            :columns="product_columns"
            :data="productAnalyticsInfo"
            :bordered="false"
          />
        </n-card>
      </n-gi>
      <n-gi :span="5">
        <n-card title="TOP 5 WORST ISSUES">
          <n-data-table
              :columns="issue_columns"
              :data="issueAnalyticsInfo"
              :bordered="false"
            />
        </n-card>
      </n-gi>
      <n-gi :span="5">
        <n-card title="TOP 5 WORST PRODUCTS PLOT">
          <div id="analytics-products">

          </div>
        </n-card>
      </n-gi>
      <n-gi :span="5">
        <n-card title="TOP 5 WORST ISSUES PLOT">
          <div id="analytics-issues">

          </div>
        </n-card>
      </n-gi>
    </n-grid>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'dashboard'
})

const product_columns = [
  {
    "title": "Name",
    "key": 'name'
  },
  {
    "title": "Amount of complaints",
    "key": 'count'
  }
]

const issue_columns = [
  {
    "title": "Cluster",
    "key": 'cluster'
  },
  {
    "title": "Amount of complaints",
    "key": 'count'
  }
]

const analytics = useAnalytics()
let productAnalyticsInfo = ref([])
let issueAnalyticsInfo = ref([])

analytics.getWorstProducts()
  .then(async (res) => {
    productAnalyticsInfo.value = res

    const Plotly = await import('plotly.js-basic-dist');

    console.log(res)

    var data = [
        {
          x: res.map(r => r.name),
          y: res.map(r => r.count),
          type: 'bar'
        }
      ];

    const layout = {
      width: 500,  // Specify the width of the plot in pixels
      height: 400  // Specify the height of the plot in pixels
    };

    Plotly.newPlot('analytics-products', data, layout);  

  })

  analytics.getWorstIssues()
  .then(async (res) => {
    issueAnalyticsInfo.value = res

    const Plotly = await import('plotly.js-basic-dist');

    var data = [
        {
          x: res.map(r => r.cluster),
          y: res.map(r => r.count),
          type: 'bar'
        }
      ];

    const layout = {
      width: 500,  // Specify the width of the plot in pixels
      height: 400  // Specify the height of the plot in pixels
    };

    Plotly.newPlot('analytics-issues', data, layout);  

  })
</script>

<style scoped>
.grid {
  row-gap: 30px !important;
  column-gap: 30px !important;
}

#analytics {
  height: 200px;
}

.plotly {
  width: 20vw !important;
  height: 500px !important;
}
</style>
