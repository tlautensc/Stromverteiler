<template>
  <div>
    <h1>Livedaten</h1>
    <md-tabs md-alignment="left">
      <md-tab md-label="Übersicht">
        <Uebersicht />
      </md-tab>
      <md-tab md-label="Spannung">
        <Spannung />
      </md-tab>
      <md-tab md-label="Strom">
        <Strom />
      </md-tab>
      <md-tab md-label="Leistung">
        <Leistung />
      </md-tab>
    </md-tabs>
  </div>
</template>

<script>
import Uebersicht from '../components/Uebersicht'
import Spannung from '../components/Spannung'
import Strom from '../components/Strom'
import Leistung from '../components/Leistung'

export default {
  name: 'Live',
  components: {
    Uebersicht,
    Spannung,
    Strom,
    Leistung,
  },
}
</script>

<style lang="scss" scoped>

</style>