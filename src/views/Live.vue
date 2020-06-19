<template>
  <div class="home">
    <h1>Live</h1>
    <div class="md-layout md-gutter md-alignment-center">
      <div class="md-layout-item md-medium-size-33 md-small-size-50 md-xsmall-size-100"></div>
      <div class="md-layout-item md-medium-size-33 md-small-size-50 md-xsmall-size-100"></div>
      <div class="md-layout-item md-medium-size-33 md-small-size-50 md-xsmall-size-100"></div>
      <div class="md-layout-item md-medium-size-33 md-small-size-50 md-xsmall-size-100"></div>
      <div class="md-layout-item md-medium-size-33 md-small-size-50 md-xsmall-size-100"></div>
      <div class="md-layout-item md-medium-size-33 md-small-size-50 md-xsmall-size-100"></div>
    </div>
    
  </div>
</template>

<script>
export default {
  name: 'Live'

}
</script>

<style lang="scss" scoped>
@import "~vue-material/dist/theme/engine"; // Import the theme engine 

  .md-layout-item {
    height: 200px;
    margin-top: 8px;
    margin-bottom: 8px;

    &:after {
      width: 100%;
      height: 100%;
      display: block;
      background: md-get-palette-color(red, 200);
      content: " ";
    }
  }
</style>