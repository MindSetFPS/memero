<script>
    import { createEventDispatcher } from "svelte"
    import TagList from "./TagList.svelte";
    import getBaseUrl from "./getBaseUrl";
    import { memesStore } from "./store";
    import MemeDetails from "./MemeDetails.svelte";
    import IntersectionObserver from "svelte-intersection-observer"

    export let post;
    export let index;
    export let filteredSearch;
    let matchingElements
    let isBigPicture = false;
    const dispatch = createEventDispatcher()
    let baseUrl = getBaseUrl()
    let element;
    let isOnScreen;

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

{#if filteredSearch.length == 0 || matchingElements.length > 0}
<IntersectionObserver {element} threshold={0.1}
    on:observe={(e) => {
        console.log(e.detail.isIntersecting)
        isOnScreen = e.detail.isIntersecting
    }}
>
    <div 
        class="
            w-full h-full
            sm:w-48 sm:h-48
            md:w-54 md:h-54
            lg:w-54 lg:h-60
            xl:w-52 xl:h-52
            2xl:w-56 2xl:h-56
            p-2
        " 
        bind:this={element} 
    >
            {#if isOnScreen }
                <div>
                    <img 
                        class="
                            object-cover
                            sm:w-48 sm:h-28
                            md:w-60 md:h-28
                            lg:w-60 lg:h-40
                            xl:w-52 xl:h-32
                            2xl:w-60 2xl:h-40 
                            hover:object-scale-down 
                            hover:mx-auto 
                            z-10 hover:z-100 transition" 
                        src="{baseUrl}/image/file/{post.filename}" 
                        alt="" 
                        on:click={ () => {
                            isBigPicture = !isBigPicture
                            console.log(isBigPicture)
                        }}
                    >
                    <div class="h-12 xl:h-12 2xl:h-8" >
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
            {:else}
                <div></div>
            {/if}
        </div>
        </IntersectionObserver>
{/if}
    