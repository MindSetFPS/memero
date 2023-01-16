<button class="rounded-lg text-white p-2 hover:{colors[type]}-800 {colors[type]}-500" on:click={handler}>
    {text}
</button>

<script>
    import { createEventDispatcher } from "svelte"

    export let type;
    export let text;

    let colors = {
        red:"bg-red",
        green:"bg-green",
        blue:"bg-blue"
    }

    const dispatch = createEventDispatcher()

    function handler(){
        dispatch('clicked')
    }
</script>