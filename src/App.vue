<template>
  <div class="page-container">
    <md-app md-waterfall md-mode="fixed">
      <md-app-toolbar class="md-primary md-small">
        <TheToolbar v-on:makeVisible="showNavigation = true"/>
      </md-app-toolbar>
      <md-app-drawer :md-active.sync="showNavigation" md-swipeable>
        <TheDrawer></TheDrawer>
      </md-app-drawer>
      <md-app-content>
        <router-view></router-view>
      </md-app-content>
    </md-app>
  </div>
</template>



<script>
  import TheDrawer from './components/TheDrawer';
  import TheToolbar from './components/TheToolbar';
  export default {
    components: {
      TheDrawer,
      TheToolbar,
    },
    name: 'Temporary',
    data: () => ({
      showNavigation: false,
    })
  }
</script>
