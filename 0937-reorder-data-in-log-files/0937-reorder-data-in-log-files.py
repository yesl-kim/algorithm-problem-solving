class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        letter_logs = []
        for log in logs:
            log = log.split(' ', 1)
            if all([x.isdigit() for x in log[1].split(' ')]):
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        
        letter_logs.sort(key=lambda x: (x[1], x[0]))
        return [' '.join(log) for log in letter_logs + digit_logs]