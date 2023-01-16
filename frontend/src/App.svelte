<script>
  import Meme from "./lib/Meme.svelte";
  import Tags from "./lib/Tags.svelte";
  import getBaseUrl from "./lib/getBaseUrl"

	async function getImages() {
    const res = await fetch(`http://127.0.0.1:5000/images`);
		const text = await res.json();
    
		if (res.ok) {
      // console.log(text)
			promise = text;
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
    console.log(event.detail.deletedId)
    const index = promise.findIndex( ({id}) => id == event.detail.deletedId)
    promise.splice(index, 1)
    promise = promise

    // promise = [...]

    // console.log('id de meme borrado: ' + result)
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
    <Tags bind:value={tags} on:tag={() => console.log(tags)} />
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
        {#each promise as post}
          <Meme filteredSearch={filteredSearch} post={post} on:meme_deleted={handleMemeDeleted}/>
        {/each}
      </div>
    {/await}
  </div>
</main>
