<script>
    export let tags
    let taglist = tags.split(",")
</script>

<div class="flex" >
    {#each taglist as tag}
    <p class="hover:bg-orange-500 px-4 mx-2 rounded-full bg-slate-400">
        {tag}
    </p>
    {/each}
</div>
