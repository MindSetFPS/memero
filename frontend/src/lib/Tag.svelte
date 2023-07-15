<script>    
    import { createEventDispatcher } from "svelte"

    export let tag

    let dispatch = createEventDispatcher()

    function handleClick(){
        dispatch('delete', {
            tag: tag
        })
    }

</script>
<div 
    class="
        hover:bg-green-600 transition font-semibold rounded-full bg-blue-400 inline-block text-white
        mx-1 px-3 py-1 my-1 text-xs"
>
{tag}

<span
    on:click={handleClick} 
    class="hover:bg-black/40 rounded-full p-1 text-xs cursor-pointer" >🚽</span>
</div>