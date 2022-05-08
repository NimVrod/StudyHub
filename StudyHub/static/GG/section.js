$(document).ready(function () {
    $(".name").click(function () {
        $.get("/GG/userinfo/" + this.id, function (data) {
            $("#name").text(data.name);
            $("#description").text(data.description);
            $("#date").text(data.date);
            $(".hidden").show(function () {
            });
            $(".container").css("animation", "lower_opacity 0.33s");

        });

    });
    $(".remove").click(function () {
        $(".hidden").hide(function () {
        });
    });

    document.addEventListener("keydown", function (e) {
        if (e.key === "Escape") {
            $(".hidden").hide(function () {
            });
        }
    });
});
