# Contributing to Audio TTS Project

Thank you for your interest in contributing! We appreciate your help in making this project better.

## 📋 Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to abide by its terms.

## 🐛 Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps which reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed after following the steps**
- **Explain which behavior you expected to see instead and why**
- **Include screenshots and animated GIFs if possible**

## ✨ Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the steps**
- **Describe the current behavior and the expected behavior**
- **Explain why this enhancement would be useful**

## 🔄 Pull Request Process

1. **Fork the repository** and create your branch from `main`
2. **Create a feature branch** for your changes:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes** and ensure code quality:
   - Write clear, commented code
   - Follow PEP 8 style guidelines
   - Add docstrings to functions and classes
4. **Test your changes thoroughly**
5. **Commit with clear messages**:

   ```bash
   git commit -m "Add feature: description of changes"
   ```

6. **Push to your fork**:

   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request** with a clear description:
   - Reference any related issues (#issue-number)
   - Describe what changes were made and why
   - Include any relevant screenshots or test results

## 📐 Code Style

### Python Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use 4 spaces for indentation
- Use meaningful variable and function names
- Add docstrings to all functions and classes

### Example

```python
def process_audio(audio_file: str, output_format: str = "wav") -> str:
    """
    Process audio file and save in specified format.
    
    Args:
        audio_file (str): Path to input audio file
        output_format (str): Output format (default: wav)
        
    Returns:
        str: Path to processed audio file
    """
    # Implementation here
    pass
```

## 🧪 Testing

- Write tests for new features
- Ensure all tests pass before submitting PR
- Run tests locally:

  ```bash
  pytest tests/
  ```

## 📦 Dependencies

- Don't add unnecessary dependencies
- If a new dependency is needed, discuss it in the issue first
- Update `requirements.txt` if adding new packages

## 📝 Commit Messages

- Use clear and descriptive commit messages
- Start with a capital letter
- Use imperative mood ("Add feature" not "Added feature")
- Keep the first line under 50 characters
- Add a blank line and more detailed explanation if needed

Example:

```text
Add Hindi language support for voice cloning

- Implement Hindi phoneme mapping
- Add language detection
- Update configuration for Hindi models
```

## 🚀 Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/audio-tts-project.git
cd audio-tts-project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r hindi-tts/requirements.txt
pip install pytest pytest-cov  # For testing

# Make your changes
# Run tests
pytest

# Push and create PR
```

## 📚 Documentation

- Update README.md if adding new features
- Add docstrings to all functions
- Include examples in your PR description
- Update relevant documentation files

## 🎯 What to Work On

Check the [Issues](https://github.com/yourusername/audio-tts-project/issues) page for:

- Bugs to fix
- Features to implement
- Documentation improvements
- Issues marked with `good first issue` for beginners

## ❓ Questions?

Feel free to:

- Open an issue with your question
- Discuss in pull request comments
- Join our community discussions

## ✅ Checklist Before Submitting PR

- [ ] Code follows style guidelines
- [ ] Tests pass locally
- [ ] No new warnings generated
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] No unrelated changes included
- [ ] PR description is detailed

---

## Thank you for contributing! 🎉
