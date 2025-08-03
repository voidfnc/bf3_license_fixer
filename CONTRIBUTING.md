# Contributing to BF3 License Fixer

Thank you for your interest in contributing to the BF3 License Fixer! This document provides guidelines for contributing to the project.

## 🚀 Quick Start

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/bf3-license-fixer.git
   cd bf3-license-fixer
   ```
3. **Set up the development environment**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Create a new branch** for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 🛠️ Development Guidelines

### Code Style
- Follow PEP 8 Python coding standards
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small

### Testing
- Test your changes thoroughly on Windows 10/11
- Ensure EA App/Origin process handling works correctly
- Verify backup and restore functionality
- Test with and without administrator privileges

### UI Guidelines
- Maintain consistency with the modern dark theme
- Ensure responsive design works across different window sizes
- Use appropriate icons and color coding for status indicators

## 📝 Types of Contributions

### 🐛 Bug Reports
When reporting bugs, please include:
- **OS Version**: Windows version and build
- **Python Version**: If running from source
- **EA Software**: EA App or Origin version
- **Error Messages**: Full error messages or screenshots
- **Steps to Reproduce**: Clear steps to reproduce the issue
- **Expected vs Actual**: What should happen vs what actually happens

### ✨ Feature Requests
When suggesting features:
- **Use Case**: Describe the problem you're trying to solve
- **Proposed Solution**: How you think it should work
- **Alternatives**: Other ways the problem could be addressed
- **Impact**: Who would benefit from this feature

### 🔧 Code Contributions
We welcome:
- **Bug fixes** for existing issues
- **UI improvements** and modernization
- **Performance optimizations**
- **New features** that enhance the core functionality
- **Documentation improvements**
- **Cross-platform support** (future scope)

## 🏗️ Project Structure

```
bf3-license-fixer/
├── 📄 main_modern.py       # Modern GUI entry point
├── 📄 launcher.py          # Interface selector
├── 📄 process_manager.py   # EA process handling
├── 📄 file_manager.py      # File operations
├── 📄 backup_manager.py    # Backup/restore logic
├── 📄 logger.py           # Logging system
├── 📁 themes/             # UI theming
│   ├── modern_theme.py    # Dark theme
│   └── icons.py          # Icon management
└── 📄 requirements.txt    # Dependencies
```

## 🔄 Pull Request Process

1. **Update Documentation**: Update README.md if needed
2. **Add Tests**: Include tests for new functionality
3. **Update Changelog**: Add entry to README changelog section
4. **Clean Commits**: Use clear, descriptive commit messages
5. **Pull Request Description**: 
   - Describe what changes you made
   - Reference any related issues
   - Include screenshots for UI changes
   - List any breaking changes

### Commit Message Format
```
type(scope): description

Examples:
fix(backup): resolve file permissions issue on restore
feat(ui): add progress animation to fix button
docs(readme): update installation instructions
```

## 🧪 Testing Your Changes

### Manual Testing Checklist
- [ ] Application launches without errors
- [ ] Modern dark UI displays correctly
- [ ] License fix process completes successfully
- [ ] Backup creation works
- [ ] Restore functionality works
- [ ] Error handling displays appropriate messages
- [ ] Administrator privilege detection works
- [ ] Process termination works safely

### Test Scenarios
1. **Normal Operation**: Run fix with EA App/Origin closed
2. **Processes Running**: Run fix with EA software running
3. **No Admin Rights**: Test behavior without administrator privileges
4. **Missing Files**: Test when license files don't exist
5. **Permission Denied**: Test when file access is restricted

## 🚨 Security Considerations

When contributing, keep in mind:
- **File System Access**: We modify system files, so be careful
- **Process Termination**: Ensure safe process handling
- **User Data**: Protect user privacy and data
- **Privilege Escalation**: Don't request unnecessary permissions

## 📚 Resources

- **Python Documentation**: https://docs.python.org/3/
- **Tkinter Documentation**: https://docs.python.org/3/library/tkinter.html
- **PSUtil Documentation**: https://psutil.readthedocs.io/
- **EA Technical Support**: For understanding EA software behavior

## 💬 Getting Help

- **GitHub Issues**: For bug reports and feature requests
- **GitHub Discussions**: For general questions and ideas
- **Code Review**: Maintainers will review your pull requests

## 📜 Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Maintain professionalism in all interactions

## 🎯 Priority Areas

Current areas where we especially welcome contributions:
- **Error handling improvements**
- **UI/UX enhancements**
- **Performance optimizations**
- **Additional safety features**
- **Better logging and diagnostics**
- **Cross-platform compatibility research**

---

Thank you for contributing to BF3 License Fixer! Your help makes the Battlefield 3 community stronger. 🎮
