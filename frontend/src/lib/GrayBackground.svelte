<div class="absolute z-10 top-0 left-0 bg-black/70 w-screen h-screen " on:click={handler}></div>


<script>
    import { createEventDispatcher } from "svelte"
    const dispatch = createEventDispatcher()

    function handler(){
        dispatch('clicked')
    }
</script>