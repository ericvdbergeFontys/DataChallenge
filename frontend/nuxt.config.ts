// https://nuxt.com/docs/api/configuration/nuxt-config
import Components from 'unplugin-vue-components/vite';
import { NaiveUiResolver } from 'unplugin-vue-components/resolvers';

export default defineNuxtConfig({
    experimental: {
        typedPages: true
    },
    css: [
        "@/assets/style/_variables.scss",
        "@/assets/style/global.scss"
    ],
    plugins: [
        '@/plugins/naive'
    ],
    modules: [
        'nuxt-icon'
    ],
    vite: {
        plugins: [
            Components({
                dts: true,
                resolvers: [NaiveUiResolver()], // Automatically register all components in the `components` directory
            }),
        ],
    },
})
