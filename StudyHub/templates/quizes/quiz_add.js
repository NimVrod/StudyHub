let questions = 2;
let answers = {
    "1": 2,
    "2": 2,
};

$("document").ready(function () {
    $("#add_question").click(function () {
        questions++;
        $("#questions").append(`
            <div class="form-group">
                <label for="question${questions}">Question ${questions}</label>
                <input type="text" class="form-control" id="question${questions}" name="question${questions}" placeholder="Question ${questions}">
            </div>
            <div class="form-group">
                <label for="answer1">Answer 1</label>
                <input type="text" class="form-control" id="answer1" name="answer1" placeholder="Answer 1">
            </div>
            <div class="form-group">
                <label for="answer2">Answer 2</label>
                <input type="text" class="form-control" id="answer2" name="answer2" placeholder="Answer 2">
            </div>
            
            <button type="button" class="btn btn-danger" id="Add Answer">Remove Question</button>
        `);

       answers[questions] = 2;
    });

    $(".add_answer").click(function () {
        answers
        $("#answers").append(`
            <div class="form-group">
                <label for="answer${answers}">Answer ${answers}</label>
                <input type="text" class="form-control" id="answer${answers}" name="answer${answers}" placeholder="Answer ${answers}">
            </div>
        `);
    });
});