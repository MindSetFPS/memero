{#if filteredSearch.length == 0 || matchingElements.length > 0}
<div class="max-w-md" >
    <img src="{baseUrl}/image/{post.filename}" alt="" on:click={bigPicture}>
    <div>
        {post.filename}
        <Tag tags={post.tags} />
    </div>
    {#if isBigPicture }
        <div class="fixed h-screen w-screen top-0 left-0" >
            <div 
                class="
                    absolute z-20 top-0 
                    bg-white
                    h-1/2 w-1/2
                    left-1/2 -translate-x-1/2 translate-y-1/2
                    p-2 rounded-lg
                    text-center
                    lg:flex
                    lg:justify-start
            ">
                <!-- <div>                   left-0  </div> -->
                    <div 
                        class="h-full w-full bg-contain bg-center bg-no-repeat " 
                        style="background-image: url({baseUrl}/image/{post.filename})"
                    >
                    </div>
                    <div class="flex flex-col justify-center font-bold  text-3xl w-full p-2">
                        <div>
                            {#if post.tags.length == 0}
                            <div>Agregar tags</div>
                            {:else}
                            <Tag tags={post.tags} />
                            {/if}
                        </div>
                        {#if showconfirmDelete}
                            De verdad quieres borrar este meme? Esto no se puede deshacer
                            <DeleteButton id={post.id} on:delete={deleteMeme} />
                        {:else}
                            <Button on:clicked={ () => showconfirmDelete = !showconfirmDelete} type="red" text="Borrar meme"   />
                        {/if}
                    </div>
                </div>
                <GrayBackground on:clicked={bigPicture} />
            </div>
    {/if}
</div>
{/if}

<script>
    import { createEventDispatcher } from "svelte"
    import GrayBackground from "./GrayBackground.svelte";
    import Button from "./Button.svelte";
    import DeleteButton from "./DeleteButton.svelte";
    import Tag from "./Tag.svelte";
    import getBaseUrl from "./getBaseUrl";

    export let post;
    export let filteredSearch;
    let matchingElements
    let isBigPicture = false;
    let showconfirmDelete = false;
    const dispatch = createEventDispatcher()


    let baseUrl = getBaseUrl()
    $: {
        // console.log(filteredSearch)
        matchingElements = filteredSearch.filter(element => post.tags.includes(element))
        // console.log(matchingElements)
    }

    function bigPicture(){
        console.log("clicked image")
        isBigPicture = !isBigPicture
    }

    async function deleteMeme(event){
        const res = await fetch(`${baseUrl}/image/delete/${event.detail.id}`);
		const text = await res.json();
    
		if (res.ok) {
      // console.log(text)
            isBigPicture = !isBigPicture
            dispatch('meme_deleted', {
                deletedId: event.detail.id
            })
		} else {
      throw new Error(text);
		}
    }

</script>