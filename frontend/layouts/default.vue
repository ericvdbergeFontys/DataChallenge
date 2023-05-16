<template>
    <div class="layout">
        <LayoutHeader />
        <aside>
            <LayoutSidebar/>
        </aside>
        <main>
            <NuxtPage/>
        </main>
    </div>
</template>

<style lang="scss">
.layout {
    display: grid;
    grid-template-columns: 200px 1fr;
    grid-template-rows: 55px 1fr;
}

.header {
    grid-row: 1;
    grid-column: 2;
}

.sidebar {
    grid-row: 1 / span 2;
    grid-column: 1;
}

main {
    grid-row: 2;
    grid-column: 2;
    padding: 30px;
}
</style>