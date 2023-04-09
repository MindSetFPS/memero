<script>
    import { createEventDispatcher } from "svelte"
    import GrayBackground from "./GrayBackground.svelte";
    import Button from "./Button.svelte";
    import DeleteButton from "./DeleteButton.svelte";
    import TagList from "./TagList.svelte";
    import getBaseUrl from "./getBaseUrl";
    import TagEditor from "./TagEditor.svelte";
    import { memesStore } from "./store";

    export let post;
    export let id;
    export let index;
    export let isBigPicture;
    let showconfirmDelete = false;
    const dispatch = createEventDispatcher()
    let baseUrl = getBaseUrl()

    function bigPicture(){
        if(isBigPicture){
            dispatch("exitBigPicture")
        }
        showconfirmDelete = false

        //copy the current list of memes
        let memesCopy = [...$memesStore]

        //sort by tag length
        memesCopy.sort( (meme1, meme2) => {
            let tags1 = meme1.tags.length
            let tags2 = meme2.tags.length
            
            if(tags1 < tags2){
                return 1
            }
            if(tags1 > tags2){
                return -1
            }
            return 0
        })
        //replace with the copy
        memesStore.update((value) =>  value = memesCopy)
    }

    async function deleteMeme(event){
        const res = await fetch(`${baseUrl}/image/delete/${event.detail.id}`);
		const text = await res.json();
    
		if (res.ok) {

            //copy the current list of memes
            const memeIndex = index
            console.log(memeIndex)
            let memesCopy = [...$memesStore]

            //edit the copy
            memesCopy.splice(memeIndex, 1)

            //replace with the copy
            memesStore.update((value) =>  value = memesCopy)
            isBigPicture = !isBigPicture
		} else {
      throw new Error(text);
		}
    }

    async function handleTagDeleted(event){

        const memeIndex = index
        //copy the current list of memes
        let memesCopy = [...$memesStore]

        //edit the copy
        memesCopy[memeIndex].tags = event.detail.taglist.toString()

        //replace with the copy
        memesStore.update((value) =>  value = memesCopy)


        //  edit in db
        const res = await fetch(`${baseUrl}/image/edit/${id}`, {
                method: "POST",
                body: JSON.stringify({
                    tags: memesCopy[memeIndex].tags
                }),
                headers: {
                    "Content-type": "application/json; charset=UTF-8"
                }
            });
            const text = await res.json();


    }
</script>

{#if isBigPicture }
<div class="fixed h-screen w-screen top-0 left-0 z-20"  >
    <div 
        class="
            absolute z-20 top-0 
            text-center bg-white p-2 rounded-lg scale-125
            h-1/2 w-1/2
            left-1/2 -translate-x-1/2 translate-y-1/2
            lg:flex lg:justify-start
    ">
        <!-- <div>                   left-0  </div> -->
        <div 
            class="h-full w-1/3 bg-contain bg-center bg-no-repeat " 
            style="background-image: url({baseUrl}/image/file/{post.filename})"
        >
        </div>
        <div class="flex flex-col justify-center font-bold w-full h-full p-2">
            {index}
            <div class="flex w-full align-middle items-center my-2">
                <div class="text-lg inline whitespace-nowrap">
                    Agregar tags
                </div>
                <TagEditor id={post.id} index={index} />
            </div>
            <div class="overflow-auto" >
                <TagList tags={$memesStore[index].tags} on:deleteTag={handleTagDeleted} />
            </div>
            {#if showconfirmDelete}
                De verdad quieres borrar este meme? Esto no se puede deshacer
                <DeleteButton id={post.id} on:delete={deleteMeme} />
            {:else}
                <Button on:clicked={ () => showconfirmDelete = !showconfirmDelete} type="red" text="Borrar meme"   />
            {/if}
        </div>
    </div>
    <GrayBackground on:clicked={bigPicture}/>
</div>
{/if}