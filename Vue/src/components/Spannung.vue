<template>
    <div>
      <div class="md-layout md-gutter md-alignment-center" style="margin: auto">
        <div class="md-layout-item md-size-33">
            <iframe src="http://localhost:3000/d-solo/bOCUe4WGz/test-dashboard?orgId=1&panelId=2&refresh=1s"  frameborder="0" scrolling="0" style="width: 100%; height: 100%; position: relative"></iframe>
        </div>
        <div class="md-layout-item md-size-33">
            <iframe src="http://localhost:3000/d-solo/bOCUe4WGz/test-dashboard?orgId=1&panelId=5&refresh=1s"  frameborder="0" scrolling="0" style="width: 100%; height: 100%; position: relative"></iframe>
        </div>
        <div class="md-layout-item md-size-33">
            <iframe src="http://localhost:3000/d-solo/bOCUe4WGz/test-dashboard?orgId=1&panelId=6&refresh=1s"  frameborder="0" scrolling="0" style="width: 100%; height: 100%; position: relative"></iframe>
        </div>
      </div>
      <div class="md-layout md-gutter md-alignment-center" style="margin: auto">
        <div class="md-layout-item md-size-100">
          <iframe src="http://localhost:3000/d-solo/bOCUe4WGz/test-dashboard?orgId=1&panelId=12&refresh=1s"  frameborder="0" scrolling="0" style="width: 100%; height: 100%; position: relative"></iframe>
        </div>
      </div>
    </div>
</template>

<script>
export default {
    name: 'Spannung'

}
</script>

<style lang="scss" scoped>
@import "~vue-material/dist/theme/engine"; // Import the theme engine 

  .md-layout-item {
    margin-top: 1vh;
    margin-bottom: 1vh;

    &:after {
      width: 100%;
      height: 100%;
    }
  }
  .md-size-33 {
    height: 35vh;
  }
  .md-size-100 {
    height: 45vh;
  }
</style>