<script>
    import { createEventDispatcher } from "svelte"
    import Tag from "./Tag.svelte";
    
    export let tags
    let taglist    

    $: {
        if(tags && tags.length > 0){
            taglist = tags.split(",")
        }
    }

    let dispatch = createEventDispatcher()

    function handleTagDeleted(event){
        const index = taglist.findIndex( (id) => id == event.detail.tag)
        taglist.splice(index, 1)
        taglist = taglist

        dispatch('deleteTag', {
            tag: event.detail.tag,
            taglist: taglist
        })
    }
</script>

<div class="relative h-full w-full text-sm overflow-auto " >
    {#if tags && tags.length > 0}
        {#each taglist as tag}
            <Tag tag={tag} on:delete={handleTagDeleted} />
        {/each}
    {/if}

    {#if tags.length == 0}
        <h1 class="text-base">Sin tags</h1>
    {/if}
</div>
