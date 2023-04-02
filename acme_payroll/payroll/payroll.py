from typing import List
from datetime import datetime

from acme_payroll.shift.shift import Shift
from acme_payroll.employee.employee import Employee
from acme_payroll.constants import PAYROLL_CALCULATED_MESSAGE, RATES, RATES_NOT_PROVIDED, WEEKDAY, WEEKEND


class PayrollService:
    def __init__(self, employees: List[Employee]):
        self.employees = employees
        self.payroll = []
        self.rates = RATES

    class Builder:
        def __init__(self, employees: List[Employee]):
            self.employees = employees
            self.payroll = []
            self.rates = RATES

        def with_rates(self, rates: dict) -> 'PayrollService.Builder':
            self.rates = rates
            return self

        def build(self) -> 'PayrollService':
            if not self.rates:
                raise Exception(RATES_NOT_PROVIDED)
            return PayrollService(self.employees)

    @staticmethod
    def _calculate_pay(self, shift: Shift) -> float:
        """
        Calculates the pay for a single shift.

        Args:
            shift (Shift): The Shift object for which to calculate the pay.
            rates (list): A list containing the hourly rates for different types of shifts.

        Returns:
            float: The total pay for the shift.
        """
        total_pay = 0

        rate_key = WEEKDAY if shift.is_weekday() else WEEKEND

        rates = self.rates[rate_key]

        for rate_period in rates:
            rate_start_time = datetime.strptime(rate_period['start'], '%H:%M')

            rate_end_time = datetime.strptime(rate_period['end'], '%H:%M')

            shift_start_time = datetime.strptime(shift.start_time, '%H:%M')

            shift_end_time = datetime.strptime(shift.end_time, '%H:%M')

            # it acts weird when the end time is 00:00, for now im setting it to 23:59
            if rate_period['end'] == '00:00':
                rate_end_time = datetime.strptime('23:59', '%H:%M')

            shiftInsideRate = rate_start_time <= shift_start_time <= rate_end_time

            shiftOverlapsRate = rate_start_time <= shift_end_time <= rate_end_time

            if shiftInsideRate or shiftOverlapsRate:
                startTime = max(shift_start_time, rate_start_time)

                endTime = min(shift_end_time, rate_end_time)

                shift_duration = endTime - startTime

                rate = rate_period['rate']

                # print('\n',startTime, endTime, shift_duration, rate)

                total_pay += shift_duration.total_seconds() / 3600 * rate

        return total_pay

    def calculate_payroll(self):
        for employee in self.employees:
            total_pay = 0

            shifts = employee.get_shifts()

            for shift in shifts:
                total_pay += self._calculate_pay(self, shift)

            self.payroll.append(
                PAYROLL_CALCULATED_MESSAGE.format(employee_name=employee.get_name(), payroll="{:.2f}".format(total_pay))
            )

        return self.payroll
