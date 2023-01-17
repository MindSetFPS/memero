<script>
  import Meme from "./lib/Meme.svelte";
  import TagSetup from "./lib/TagSetup.svelte";
  import getBaseUrl from "./lib/getBaseUrl"
  import { memesStore } from "./lib/store";

	async function getImages() {
    const res = await fetch(`http://127.0.0.1:5000/images`);
		const text = await res.json();
    
		if (res.ok) {
      memesStore.set(text)      
		} else {
      throw new Error(text);
		}
	}
  
  async function handleUpload(event){
    // console.log(files)
    const formData = new FormData()
    for (let i = 0; i < files.length; i++){
      console.log(files[i].name)
      formData.append('file', files[i])
    }
    formData.append('tags', tags)
    
    const res = await fetch(baseUrl + '/', {
      method: 'POST',
      body: formData
    })
    // const text = await res.json()

    if (res.ok) {
      getImages()
      event.target.reset()
		}
  }

  function handleSearh(){
    filteredSearch = search.split(",")
  }

  function handleMemeDeleted(event){

    //copy the current list of memes
    const memeIndex = event.detail.index
    let memesCopy = [...$memesStore]

    //edit the copy
    memesCopy.splice(memeIndex, 1)

    //replace with the copy
    memesStore.update((value) =>  value = memesCopy)
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

  let posts;
  let files;
  let tags;
  let search;
  let filteredSearch = []
  let promise = []
  let baseUrl = getBaseUrl()
  getImages()
</script>

<main class="p-4">
  <h1 class="text-5xl font-bold">Your memes sir</h1>
  <div>
    <input 
      type="text" 
      name="filter" 
      id="filter" 
      placeholder="buscar meme" 
      bind:value={search} 
      on:input={handleSearh}
    >
    <p class="flex">
      {#each filteredSearch as t}
        <div class="p-2 bg-blue-300 rounded-md m-2">
          {t}
        </div>
      {/each}
    </p>
  </div>

  <form action="/" method="post" enctype="multipart/form-data" on:submit|preventDefault={handleUpload} >
    <input type="file" id="myFile" name="file" bind:files multiple >
    <input type="submit" value="Upload">
    <TagSetup bind:value={tags} on:tag={() => console.log(tags)} />
  </form>
  <div>
    {#await promise}
      <h1>Loading</h1>
    {:then promise}
      <div 
        class="
          grid gap-3
          grid-cols-3
          md:grid-cols-4
          lg:grid-cols-5
          xl:grid-cols-6
          2xl:grid-cols-8
      ">
        {#each $memesStore as post, index}
          <Meme 
            filteredSearch={filteredSearch} 
            post={post}
            index={index}
            on:meme_deleted={handleMemeDeleted}
            on:deleteTag={handleTagDeleted}
          />
        {/each}
      </div>
    {/await}
  </div>
</main>
