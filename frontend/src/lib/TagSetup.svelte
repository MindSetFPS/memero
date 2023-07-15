<script>
    import { createEventDispatcher } from "svelte"

    const dispatch = createEventDispatcher()

    export let value = []
    let currentTag = ''
    function addTag(){
        value = [...value, currentTag]
        currentTag=''
        dispatch('tag')
        console.log(value)
    }

</script>
<div class="p-2" >
    <input type="text" name="tag" id="tags" placeholder="agregar tags" bind:value={currentTag} />
    <button on:click|preventDefault={addTag} class="p-2 bg-gray-200 hover:bg-gray-300 rounded-md" > Add </button>
    {#each value as tag}
    <div class="">
        {tag}
    </div>
    {/each}
</div>