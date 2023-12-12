class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        new_dirs = []
        
        for d in dirs:
            if not d or d == '.':
                continue
            
            if d == '..':
                if new_dirs:
                    new_dirs.pop()
                continue
            
            new_dirs.append(d)
        
        return '/' + '/'.join(new_dirs)