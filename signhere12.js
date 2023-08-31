export default {
  template: `
<div id="app" class="flex items-center justify-center">
  <form ref="form" class="signature-pad-form bg-white p-8 shadow-md rounded-lg w-96">
    <h1 class="text-2xl font-semibold mb-4">Important Contract</h1>
    <p class="text-gray-600 mb-4">Important contract description</p>
    <p class="mb-2"><b>Signature</b></p>
    <canvas
      @pointerdown.passive="handlePointerDown"
      @pointerup.passive="handlePointerUp"
      @pointermove.passive="handlePointerMove"
      ref="canvas" height="100" width="300" class="signature-pad border border-gray-300 mb-4"></canvas>
    <p>
      <a
        @click.prevent="clearPad"
        href="#" class="clear-button text-blue-500 hover:underline">Clear</a>
    </p>
    <button
      @click.prevent="submit"
      class="submit-button bg-blue-500 hover:bg-blue-600 text-white font-semibold px-4 py-2 rounded-md mt-4">
      SUBMIT
    </button>
    <button
      @click.prevent="$emit('close')"
      class="submit-button bg-blue-500 hover:bg-blue-600 text-white font-semibold px-4 py-2 rounded-md mt-4">
      Close
    </button>
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
      positionY: null
    };
  },
  methods: {
    handlePointerDown(event)  {
      this.write = true;
      this.ctx.beginPath();
      const [positionX, positionY] = this.getCursorPosition(event);
      this.ctx.moveTo(positionX, positionY);
    },
    handlePointerUp()  {
      this.write = false;
    },
    handlePointerMove(event)  {
      if (!this.write) return;
      const [positionX, positionY] = this.getCursorPosition(event);
      this.ctx.lineTo(positionX, positionY);
      this.ctx.stroke();
    },
    getCursorPosition(event)  {
      const positionX = event.clientX - event.target.getBoundingClientRect().x;
      const positionY = event.clientY - event.target.getBoundingClientRect().y;
      return [positionX, positionY];
    },
    clearPad()  {
      this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    },
    submit()  {
      const imageURL = this.canvas.toDataURL();
      this.$emit("change", imageURL);
      this.clearPad();
    },
  },
  props: {},
  mounted() {
    this.canvas = this.$refs["canvas"];
    this.ctx = this.canvas.getContext("2d");
  },
};
