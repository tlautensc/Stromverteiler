<template>
      <md-app-drawer md-swipeable>
        <md-toolbar class="md-transparent" md-elevation="0">
          Navigation
        </md-toolbar>

        <md-list>
          <md-list-item>
            <md-button to="/home">Home</md-button>
          </md-list-item>

          <md-list-item>
            <span class="md-list-item-text">Trash</span>
          </md-list-item>

          <md-list-item>
            <span class="md-list-item-text">Spam</span>
          </md-list-item>
        </md-list>
      </md-app-drawer>
</template>

<script>
export default {
    name: 'TheDrawer',
    data: () => ({
      showNavigation: true,
    })
}
</script>

<style>

</style>