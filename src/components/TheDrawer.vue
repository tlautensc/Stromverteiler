<template>
  <div>
    <md-toolbar class="md-transparent" md-elevation="0">
      Navigation
    </md-toolbar>

    <md-list>
      <md-list-item>
        <md-button to="/home" @click.native="makeInvisible()">Home</md-button>
      </md-list-item>

      <md-list-item>
        <md-button to="/live" @click.native="makeInvisible()">Live</md-button>
      </md-list-item>

      <md-list-item>
        <md-button to="/history" @click.native="makeInvisible()">History</md-button>
      </md-list-item>
    </md-list>
  </div>
</template>

<script>
export default {
    name: 'TheDrawer',
    methods: {
      makeInvisible() {
        this.$emit('makeInvisible')
      }
    },
}
</script>

<style>
.md-drawer {
    width: 230px;
    max-width: calc(100vw - 125px);
  }
</style>
