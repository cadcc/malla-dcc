<template>
  <div class="flex items-center pt-4 pr-2">
    <label for="toogleA" class="flex items-center cursor-pointer">
      <div class="relative">
        <input
          id="toogleA"
          type="checkbox"
          class="hidden"
          @change="$store.dispatch('toggleDarkMode')"
        />
        <div
          class="w-10 h-4 bg-gray-400 rounded-full shadow-inner toggle__line"
        ></div>
        <div
          class="absolute inset-y-0 left-0 w-6 h-6 bg-white rounded-full shadow toggle__dot"
        ></div>
      </div>
      <div class="ml-3 font-medium text-gray-700">
        {{ value ? '🌙' : '☀️' }}
      </div>
    </label>
  </div>
</template>

<style scoped>
.toggle__dot {
  top: -0.25rem;
  left: -0.25rem;
  transition: all 0.3s ease-in-out;
}

input:checked ~ .toggle__dot {
  transform: translateX(100%);
  background-color: #1f2937;
}
</style>

<script>
export default {
  props: {
    value: {
      type: Boolean,
      required: true,
    },
  },
};
</script>
