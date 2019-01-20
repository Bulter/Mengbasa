$(function () {
//	二维码隐藏事件
    $(".top_in a,.bot_copy .bot_copya").hover(function () {
        if ($(this).children().has('div') || $(this).siblings().has('.copy_in')) {
            $(this).children("div").show();
            $(this).siblings('.copy_in').show();
        }
    }, function () {
        $(this).children("div").hide();
        $(this).siblings('.copy_in').hide();
    });

//  底部导航鼠标移入事件
    $(".copy_in").mouseenter(function () {
        $(this).show();
    }).mouseleave(function () {
        $(this).hide();
    })


//横向菜单导航栏
    $('.nav_in li a').find("img").mouseenter(function () {
        var _src = $(this).attr('src');
        var _hsrc = $(this).attr('hsrc')
        $(this).attr('psrc', _src);
        $(this).attr('src', _hsrc);
    }).mouseleave(function () {
        var _psrc = $(this).attr('psrc')
        $(this).attr('src', _psrc);
    })
//横向菜单导航栏结束


//竖向菜单栏
    $('.slionav_left ul').find('li').hover(function () {
        $(this).find('h3 a').css('color', 'white');
        var index = $(this).index();
        $(this).removeClass('lihover').addClass('lihover').siblings('li').removeClass('lihover');
        $(this).parent().parent().siblings('.slionav_right').find('ul').eq(index).show().siblings('ul').hide();
    }, function () {
        $(this).find('h3 a').css('color', 'black');
        $(this).removeClass('lihover');
        $(this).parent().parent().siblings('.slionav_right').find('ul').hide();
    });

    $('.slionav_right').find("ul").mouseenter(function () {
        $(this).show();
        var index = $(this).index();
        $(this).parent().siblings('.slionav_left').find('li').eq(index).removeClass('lihover').addClass('lihover');
    }).mouseleave(function () {
        $(this).hide();
        $(this).parent().siblings('.slionav_left').find('li').removeClass('lihover');
    });
    //竖向菜单栏结束

    //轮播图开始
    var topSwiper = new Swiper('#topSwiper', {
        pagination: '.swiper-pagination',
        slidesPerView: 1,
        paginationClickable: true,
        spaceBetween: 30,
        loop: true,
        autoplay: 3000,

        effect: 'coverflow',
        grabCursor: true,
        coverflow: {
            shadow: true,
            slideShadows: true,
            shadowOffset: 20,
            shadowScale: 0.94
        }
    });
    //轮播图结束
});
