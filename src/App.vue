<template>
  <div class="page-container">
    <md-app md-waterfall md-mode="fixed">
      <md-app-toolbar class="md-primary md-small">
        <div class="md-toolbar-row">
          <div class="md-toolbar-section-start" @click="showNavigation = true">
            <md-button class="md-icon-button">
              	<md-icon>menu</md-icon>
            </md-button>
          </div>
        </div>
        <div class="md-toolbar-row md-toolbar-offset">
          <h3 class="md-title">Tontechnik Butz</h3>
        </div>
      </md-app-toolbar>

      <TheDrawer></TheDrawer>

      <md-app-content>
        <router-view></router-view>
      </md-app-content>
    </md-app>
  </div>
</template>



<script>
  import TheDrawer from './components/TheDrawer.vue'
  export default {
    components: {
      TheDrawer,
    },
    name: 'Temporary',
    data: () => ({
      showNavigation: false,
    })
  }
</script>

<style lang="scss" scoped>
  .md-app {
    max-height: 400px;
    min-height: 400px;
    border: 1px solid rgba(#000, .12);
  }

   // Demo purposes only
  .md-drawer {
    width: 150px;
    max-width: calc(100vw - 125px);
  }
</style>