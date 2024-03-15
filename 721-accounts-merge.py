class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict


        graph = defaultdict(set)
        email_to_name = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                graph[account[1]].add(email)
                graph[email].add(account[1])
                email_to_name[email] = name


        visited = set()
        merged_accounts = []
        for email in graph:
            if email not in visited:
                stack = [email]
                emails = []
                while stack:
                    node = stack.pop()
                    if node not in visited:
                        visited.add(node)
                        emails.append(node)
                        for neighbor in graph[node]:
                            stack.append(neighbor)

                emails.sort()
                merged_accounts.append([email_to_name[email]] + emails)
        return merged_accounts
