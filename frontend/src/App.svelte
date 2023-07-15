<script>
  import Meme from "./lib/Meme.svelte";
  import getBaseUrl from "./lib/getBaseUrl"
  import { memesStore } from "./lib/store";
  import UploadMemes from "./lib/UploadMemes.svelte";
  import { infiniteScrollObserver } from "./lib/loadOnLastItem";

  let posts;
  let page = 1;
  let search;
  let filteredSearch = []
  let promise = []
  let baseUrl = getBaseUrl()

	async function getImages(){
    const res = await fetch(`${baseUrl}/images/${page}`);
		const text = await res.json();
    
    if(page == 1){
      if (res.ok) {
        console.log(text)
        memesStore.set(text)
      } else {
        throw new Error(text);
      }
    } else {
      if (res.ok) {
        console.log(text)
        $memesStore = [...$memesStore, ...text]
      } else {
        throw new Error(text);
      }
    }
    page = page + 1
	}
  
  function handleSearh(){
    filteredSearch = search.split(",")
  }
  
  function handleTagDeleted(event){
    // console.log(event.detail.memeId, event.detail.tag, event.detail.index, event.detail.taglist)
    
    const memeIndex = event.detail.index
    //copy the current list of memes
    let memesCopy = [...$memesStore]
    
    //edit the copy
    memesCopy[memeIndex].tags = event.detail.taglist.toString()
    
    //replace with the copy
    memesStore.update((value) =>  value = memesCopy)
  }

  let observedElement = null

  const load = () => {
    setTimeout(() => {
      getImages()
    }, 400)
  }

  $:{
    if(observedElement){
      infiniteScrollObserver({fetch: load, observedElement: observedElement})
    }
  }

  getImages()
</script>

<main class="p-4" >
  <div class="block lg:flex align-middle items-center w-full">
    <h1 class="text-5xl font-bold whitespace-nowrap">Your memes sir</h1>
      <input 
        type="text" 
        name="filter" 
        id="filter" 
        class="p-2 m-2 rounded-lg bg-gray-200 placeholder:text-gray-500 hover:bg-gray-300 transition "
        placeholder="buscar meme" 
        bind:value={search} 
        on:input={handleSearh}
      >
      <p class="flex overflow-auto">
        {#each filteredSearch as t}
        <div class="p-2 bg-blue-300 rounded-md m-2">
          {t}
        </div>
        {/each}
      </p>
  </div>

  <div>
    {#await promise}
      <h1>Loading</h1>
    {:then promise}
      <UploadMemes on:filesUploaded={getImages} />
      <div 
        class="
          grid gap-0
          grid-cols-2
          sm:grid-cols-3
          md:grid-cols-4
          lg:grid-cols-5
          xl:grid-cols-6
          2xl:grid-cols-7
      ">
        {#each $memesStore as post, index}
          <Meme 
            filteredSearch={filteredSearch} 
            post={post}
            index={index}
            on:deleteTag={handleTagDeleted}
          />
        {/each}

        {#if $memesStore.length == 0}
          <h1 class="w-screen h-screen flex justify-center align-middle items-center font-bold text-6xl">
            Sube tu primer meme 🤡
          </h1>
        {/if}
      </div>
    {/await}
  </div>
  <footer bind:this={observedElement}>
    <h1>Llegaste hasta el final</h1>
  </footer>
</main>
