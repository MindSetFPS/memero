<button class="rounded-lg text-black p-2  {colors[type]}" on:click={handler}>
    {text}
</button>

<script>
    import { createEventDispatcher } from "svelte"

    export let type;
    export let text;

    let colors = {
        red:"hover:bg-red-800 bg-red-500 text-white",
        green:"hover:bg-green-800 bg-green-500 text-white",
        blue:"hover:bg-blue-800 bg-blue-500 text-white"
    }

    const dispatch = createEventDispatcher()

    function handler(){
        dispatch('clicked')
    }
</script>