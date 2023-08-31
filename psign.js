export default {
  template: `
<div class="flex items-center justify-center max-h-[90vh] overflow-hidden">
  <form ref="form" class="bg-white py-8 px-4 shadow-md rounded-lg w-full">
    <p class="mb-2 text-center w-full"><b>Signature</b></p>
    <canvas
      @pointerdown.passive="handlePointerDown"
      @pointerup.passive="handlePointerUp"
      @pointermove.passive="handlePointerMove"
      ref="canvas" :height="height" width="300" class="signature-pad border border-gray-300 mb-4" style="touch-action: none;"></canvas>
      
      <div class="flex justify-between w-full">
          <button @click.prevent="clearPad" class="text-sm border border-gray-600 text-gray-600 hover:text-gray-900 hover:border-gray-900 px-4 py-2 rounded">Clear</button>
          <button @click.prevent="submit" class="text-sm border border-blue-500 text-blue-500 hover:text-white hover:bg-blue-500 px-4 py-2 rounded">Save</button>
          <button @click.prevent="$emit('close')" class="text-sm border border-red-500 text-red-500 hover:text-white hover:bg-red-500 px-4 py-2 rounded">Close</button>
      </div>

  </form>
</div>


  `,
  data() {
    return {
      write: false,
      ctx: null,
      canvas: null,
      showImage: false,
      positionX: null,
      positionY: null,
      height: window.innerHeight * 0.7,
    };
  },

  methods: {
    handlePointerDown(event) {
      this.write = true;
      this.ctx.beginPath();
      const [positionX, positionY] = this.getCursorPosition(event);
      this.ctx.moveTo(positionX, positionY);
    },
    handlePointerUp() {
      this.write = false;
    },
    handlePointerMove(event) {
      if (!this.write) return;
      const [positionX, positionY] = this.getCursorPosition(event);
      this.ctx.lineTo(positionX, positionY);
      this.ctx.stroke();
    },
    getCursorPosition(event) {
      const positionX = event.clientX - event.target.getBoundingClientRect().x;
      const positionY = event.clientY - event.target.getBoundingClientRect().y;
      return [positionX, positionY];
    },
    clearPad() {
      this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    },
    submit() {
      const imageURL = this.canvas.toDataURL();
      this.$emit("change", imageURL);
      this.clearPad();
      this.$emit("close");
    },
  },
  props: {},
  mounted() {
    this.canvas = this.$refs["canvas"];
    this.ctx = this.canvas.getContext("2d");
  },
};
