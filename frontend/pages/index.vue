<template>
    <div>
            <div class="layout">
                <n-grid x-gap="12" :cols="3">
                    <n-gi :span="2" class="container">
                        <n-h1>Place your reviews on our trusted platform!</n-h1>
                        <img src="/reviews-banner.png"/>
                        <n-select
                            v-model:value="selectedProduct"
                            placeholder="Select"
                            :options="products"
                            size="large"
                        />
                        <n-input
                            maxlength="200"
                            type="textarea"
                            placeholder="What do you want to review?"
                            v-model:value="reviewText"
                        />
                        <n-button @click="sendReview" type="info" style="height: 40px;">
                            <n-spin v-show="sendingReview" :size="20" class="n-spin" stroke="white" />
                            Send your review!
                        </n-button>
                    </n-gi>
                    <n-gi>
                        <n-card
                            title="Classification"
                            :segmented="{
                                content: true,
                            }"
                        >
                            <n-spin v-if="sendingReview" size="large" style="width: 100%; margin: 0 auto; padding: 20px;" stroke="black" />
                            <n-data-table
                                v-else
                                :columns="columns"
                                :data="[classification]"
                                :bordered="false"
                            />
                        </n-card>
                    </n-gi>
                </n-grid>
            </div>
    </div>
</template>

<script setup>
definePageMeta({
  layout: 'default'
})

// let hasSendReview = ref(false)
let sendingReview = ref(false)

// fetch products =================================
const products = useProducts();

// bindable properties =================================
let selectedProduct = ref()
let reviewText = ref()

let classification = ref({
    cluster: "-",
    emotion: "-",
    sentiment: "-"
}) 

const columns = [{title: "cluster", key: "cluster", width: 100}, {title:"emotion", key: "emotion", width: 100}, {title:"sentiment", key: "sentiment", width: 100}]


// functions  =================================
const sendReview = async () => {
    sendingReview.value = true
    const createdReviews = await $fetch('http://localhost:8000/reviews', {
        method: 'POST',
        body:  {
            productName: selectedProduct.value,
            text: reviewText.value
        }
    })
    sendingReview.value = false
    classification.value = {
        cluster: createdReviews[0].cluster,
        emotion: createdReviews[0].emotion,
        sentiment: createdReviews[0].sentiment
    }
}
</script>

<style scoped>
    .layout {
        width: 70vw;
        margin: 0 auto;
    }
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100% !important;
        margin: 0 auto;
        gap: 20px;   
    }

    .n-h1 {
        font-size: 1vw;
        line-height: 0.95;
        margin-top: 40px;
    }

    img {
        width: 100%;
        height: 200px;
        object-fit: cover;
        object-position: center -40px;
    }

    .n-input {
        min-height: 20vh;
        font-size: 16px;
    }

    .n-spin {
        margin: 0 auto;
        margin-right: 20px !important;
    }

    .container * {
        width: 100%;
    }

    .n-card {
        margin-top: 20vh;
        margin-left: 30px;
        display: flex;
        justify-content: center;
    }
</style>