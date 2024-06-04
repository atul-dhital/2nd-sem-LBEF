$(() => {
	pageTitleSorter();
	bsEvents();
})

function bsEvents() {
	$(window).resize(function () {
		var mql = window.matchMedia("(max-width: 600px)")
		if (mql.matches) {
			$('[data-toggle="tooltip"]').tooltip('show')
		}
	});
}

function pageTitleSorter() {
	var url = window.location.href;

	let splitUrl = url.split('/'),
		composedUrl = splitUrl[splitUrl.length - 1].split('.')[0];
	$('.side-nav .list-group').find('.list-group-item:contains(' + composedUrl + ')').addClass('active');
	$('.page-title').html(composedUrl);
}

    document.getElementsByClassName('.btn').style.backgroundColor = '#3bae12';
    document.getElementsByClassName('.btn').style.borderColor = '#3bae12';
