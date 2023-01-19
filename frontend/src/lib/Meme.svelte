{#if filteredSearch.length == 0 || matchingElements.length > 0}
<div class="max-w-md" >
    <img src="{baseUrl}/image/{post.filename}" alt="" on:click={ () => {
        isBigPicture = !isBigPicture
        console.log(isBigPicture)
        }}>
    <div>
        <p class="whitespace-nowrap overflow-hidden overflow-ellipsis">
            {post.filename}
        </p>
        <TagList tags={$memesStore[index].tags} on:deleteTag={handleTagDeleted} />
    </div>
    <MemeDetails 
        on:deleteTag={handleTagDeleted} 
        on:exitBigPicture={ () => isBigPicture = !isBigPicture} 
        index={index} 
        id={post.id}
        post={post}
        isBigPicture={isBigPicture}
        />
    </div>
    {/if}
    
    <script>
    import { createEventDispatcher } from "svelte"
    import TagList from "./TagList.svelte";
    import getBaseUrl from "./getBaseUrl";
    import { memesStore } from "./store";
    import MemeDetails from "./MemeDetails.svelte";

    export let post;
    export let index;
    export let filteredSearch;
    let matchingElements
    let isBigPicture = false;
    const dispatch = createEventDispatcher()
    let baseUrl = getBaseUrl()

    $: {
        matchingElements = filteredSearch.filter(element => post.tags.includes(element))
    }

    function handleTagDeleted(event){
        dispatch('deleteTag', {
            tag: event.detail.tag,
            index: index,
            memeId: post.id,
            taglist: event.detail.taglist
        })  
    }

</script>