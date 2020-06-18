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

      <md-app-drawer :md-active.sync="showNavigation" md-swipeable>
        <md-toolbar class="md-transparent" md-elevation="0">
          Navigation
        </md-toolbar>

        <md-list>
          <md-list-item>
            <md-button to="/home">Home</md-button>
          </md-list-item>

          <md-list-item>
            <span class="md-list-item-text">Sent Mail</span>
          </md-list-item>

          <md-list-item>
            <span class="md-list-item-text">Trash</span>
          </md-list-item>

          <md-list-item>
            <span class="md-list-item-text">Spam</span>
          </md-list-item>
        </md-list>
      </md-app-drawer>

      <md-app-content>
        <router-view></router-view>
      </md-app-content>
    </md-app>
  </div>
</template>

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


<script>
  export default {
    name: 'Temporary',
    data: () => ({
      showNavigation: false,
      showSidepanel: false
    })
  }
</script>