<template>
  <div class="page-container">
    <md-app md-waterfall md-mode="fixed">
      <md-app-toolbar class="md-primary md-small">
        <TheToolbar v-on:makeVisible="showNavigation = true"/>
      </md-app-toolbar>
      <md-app-drawer :md-active.sync="showNavigation" md-swipeable>
        <TheDrawer v-on:makeInvisible="showNavigation = false"/>
      </md-app-drawer>
      <md-app-content>
        <router-view></router-view>
      </md-app-content>
    </md-app>
  </div>
</template>

<script>
import TheDrawer from './TheDrawer'
import TheToolbar from './TheToolbar'
export default {
    name: 'Computer',
    components: {
        TheDrawer,
        TheToolbar,
    },
    data: () => ({
      showNavigation: false,
    })

}
</script>

<style>

</style>