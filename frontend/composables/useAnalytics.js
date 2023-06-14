export const useAnalytics = ()  => {
    return new Analytics()
}

class Analytics {
    getForProduct = async (productName) => {
        return await $fetch('http://localhost:8000/analytics/product', {
            method: 'POST',
            body: { productName: productName }
        })
    }
    getWorstProducts = async () => {
        return await $fetch('http://localhost:8000/analytics/worst-products')
    }
    getWorstIssues = async () => {
        return await $fetch('http://localhost:8000/analytics/worst-issues')
    }
}