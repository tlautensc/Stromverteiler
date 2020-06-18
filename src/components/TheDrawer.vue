<template>
  <div>
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
  </div>
</template>

<script>
export default {
    name: 'TheDrawer',
}
</script>

<style>


</style>
