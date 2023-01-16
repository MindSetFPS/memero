<script>
    import { createEventDispatcher } from "svelte"
    import Button from "./Button.svelte";
    export let id;

    const dispatch = createEventDispatcher()

    function handler(){
        dispatch('delete', {
            id: id
        })
    }
</script>

<Button type="red" on:clicked={handler} text="Borrar para siempre" />