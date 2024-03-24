<script setup lang="ts">
import Weather from "./components/Weather.vue";
import Header from "./components/parts/Header.vue";
</script>

<template>
  <v-app>
    <Header />
    <v-main>
      <Weather />
    </v-main>
  </v-app>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
