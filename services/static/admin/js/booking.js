(function($) {
    $(document).ready(function() {
        function updateTotalCost() {
            var selectedWorker = $("#id_worker option:selected");
            var hourlyRate = parseFloat(selectedWorker.data("rate")) || 0;
            var duration = parseInt($("#id_duration").val()) || 0;
            var totalCost = hourlyRate * duration;
            
            $("#id_total_cost").val(totalCost.toFixed(2)); // Auto-update total cost
            $("#worker-hourly-rate").text(hourlyRate.toFixed(2)); // Show hourly rate
        }

        // Run function on change
        $("#id_worker, #id_duration").change(updateTotalCost);

        // Run on page load
        updateTotalCost();
    });
})(django.jQuery);
